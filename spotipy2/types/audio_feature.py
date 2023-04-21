from __future__ import annotations
from dataclasses import dataclass

from spotipy2 import types


@dataclass
class AudioFeature(types.BaseType):
    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: int
    energy: float
    id: str
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    speechiness: float
    tempo: float
    time_signature: int
    track_href: str
    type: str
    uri: str
    valence: float

    def bpm(self) -> int:
        return self.tempo

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"AudioFeature(id='{self.id}')"
