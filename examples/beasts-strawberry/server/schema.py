""" This file was code generated by turms. If you want to change the contents of this file, you should make sure to add the MergeProcessor to your config will keep your changes when you re-run turms)."""

from enum import Enum
from typing import AsyncGenerator, List, Optional

import strawberry


@strawberry.input
class BeastInput:
    id: Optional[str]
    legs: Optional[int]
    binomial: Optional[str]
    common_name: Optional[str]
    tax_class: Optional[str]
    eats: Optional[List[Optional[str]]]


@strawberry.input
class CountryInput:
    id: Optional[str]
    nana: Optional[str]


@strawberry.type
class Beast:
    id: Optional[str] = strawberry.field(
        description="ID of beast (taken from binomial initial)"
    )
    legs: Optional[int] = strawberry.field(description="number of legs beast has")
    binomial: Optional[str] = strawberry.field(description="a beast's name in Latin")
    common_name: Optional[str] = strawberry.field(
        description="a beast's name to you and I"
    )
    tax_class: Optional[str] = strawberry.field(description="taxonomy grouping")
    eats: Optional[List[Optional["Beast"]]] = strawberry.field(
        description="a beast's prey"
    )
    is_eaten_by: Optional[List[Optional["Beast"]]] = strawberry.field(
        description="should be a beast, but can be a plant"
    )
    farts: Optional[bool] = strawberry.field(description="farts a lot")
    maybe_ne_farts: Optional[bool]


@strawberry.type
class Query:
    @strawberry.field(description="get all the beasts on the server")
    def beasts(self) -> Optional[List[Optional[Beast]]]:
        """get all the beasts on the server"""
        return None

    @strawberry.field()
    def beast(self, id: str) -> Beast:
        return None

    @strawberry.field()
    def called_by(self, common_name: str) -> List[Optional[Beast]]:
        return None


@strawberry.type
class Mutation:
    @strawberry.mutation(description="create a massive beast on the server")
    def create_beast(
        self,
        id: str,
        legs: int,
        binomial: str,
        common_name: str,
        tax_class: str,
        eats: Optional[List[Optional[str]]],
    ) -> Beast:
        """create a massive beast on the server"""
        return None

    @strawberry.mutation()
    def create_beast_input(self, beast: BeastInput) -> Beast:
        return None


@strawberry.type
class Subscription:
    @strawberry.subscription()
    async def watch_beast(self, id: str) -> AsyncGenerator[Optional[Beast], None]:
        return None