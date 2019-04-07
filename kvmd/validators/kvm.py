# ========================================================================== #
#                                                                            #
#    KVMD - The main Pi-KVM daemon.                                          #
#                                                                            #
#    Copyright (C) 2018  Maxim Devaev <mdevaev@gmail.com>                    #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
#                                                                            #
# ========================================================================== #


from typing import Any

from . import check_string_in_list

from .basic import valid_number


# =====
def valid_atx_button(arg: Any) -> str:
    return check_string_in_list(arg, "ATX button", ["power", "power_long", "reset"])


def valid_kvm_target(arg: Any) -> str:
    return check_string_in_list(arg, "KVM target", ["kvm", "server"])


def valid_log_seek(arg: Any) -> int:
    return int(valid_number(arg, min=0, name="log seek"))


def valid_stream_quality(arg: Any) -> int:
    return int(valid_number(arg, min=1, max=100, name="stream quality"))


def valid_stream_fps(arg: Any) -> int:
    return int(valid_number(arg, min=0, max=30, name="stream FPS"))