# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Union

from pydantic import AnyHttpUrl, BaseModel
from pydantic.fields import Field
from submodules.fastapi_haljson.src.halmodel import HALBase


class RepoInternal(BaseModel):
    routes: dict[str, str]


class RepoAPIInfo(BaseModel):
    name: str
    method: str


class RepoErrorResponse(HALBase):
    message: str = Field(
        ...,
        description="Error message",
    )
    location: str = Field(
        ...,
        description="Error location",
    )
    param: str = Field(
        ...,
        description="Parameters of request",
    )
    value: Union[
        tuple[list[str], int],
    ] = Field(
        ...,
        description="Values of request",
    )
    error: str = Field(
        ...,
        description="Error type",
    )
