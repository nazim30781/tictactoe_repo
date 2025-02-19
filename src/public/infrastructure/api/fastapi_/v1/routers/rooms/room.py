from dataclasses import dataclass, field
from uuid import uuid4

from fastapi import WebSocket


@dataclass
class RoomPlayer:
    player_oid: str
    name: str | None = field(default=None)
    websocket: WebSocket | None = field(default=None)


@dataclass
class Room:
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    player_1: RoomPlayer | None = field(default=None)
    player_2: RoomPlayer | None = field(default=None)
    game_oid: str | None = field(default=None)
    start: bool = field(default=False)

    def is_empty(self) -> bool:
        if self.player_2:
            return False

        return True

    def check_player(self, websocket: WebSocket) -> bool:
        if self.player_1.websocket == websocket or self.player_2.websocket == websocket:
            return True

        return False


class RoomsManager:
    def __init__(self):
        self.__rooms: list[Room] = list()

    def __check_player(self, websocket: WebSocket):
        for room in self.__rooms:
            if room.check_player(websocket):
                return room

        return False

    def __get_empty_room(self) -> Room | None:
        for room in self.__rooms:
            if room.player_2 is None:
                return room

    def __create_room(self, player_oid: str, player_name: str) -> Room:
        room = Room(player_1=RoomPlayer(player_oid, player_name))

        return room

    def connect_player(self, player_oid: str, player_name: str = None) -> Room:
        room = self.__get_empty_room()

        if room:
            room.player_2 = RoomPlayer(player_oid, player_name)
            return room
        else:
            room = self.__create_room(player_oid, player_name)
            self.__rooms.append(room)
            return room

    def get_room_by_id(self, oid: str):
        for room in self.__rooms:
            if room.oid == oid:
                return room

    def start(
        self, room: Room, websocket: WebSocket, player_oid: str, player_name: str = None
    ) -> bool:
        if room.player_1.player_oid == player_oid:
            room.player_1.websocket = websocket
            return False
        else:
            print("yes")
            room.player_2.websocket = websocket
            return True

    @staticmethod
    def check_room_is_full(self, room: Room):
        if room.player_1 and room.player_2:
            return True

    def get_rooms(self):
        print(self.__rooms)
