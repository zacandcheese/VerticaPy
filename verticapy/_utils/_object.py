"""
Copyright  (c)  2018-2024 Open Text  or  one  of its
affiliates.  Licensed  under  the   Apache  License,
Version 2.0 (the  "License"); You  may  not use this
file except in compliance with the License.

You may obtain a copy of the License at:
http://www.apache.org/licenses/LICENSE-2.0

Unless  required  by applicable  law or  agreed to in
writing, software  distributed  under the  License is
distributed on an  "AS IS" BASIS,  WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.
See the  License for the specific  language governing
permissions and limitations under the License.

This file was created to avoid circular import and to
locate all  the  inner functions imports in only  one
single file.  No other file should have inner imports.
"""
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from verticapy.core.vdataframe.base import vDataColumn, vDataFrame
    import verticapy.machine_learning.vertica as vml


def create_new_vdc(*args, **kwargs) -> "vDataColumn":
    """
    Creates a :py:class:`vDataColumn`.

    .. note::

        This function is used to bring main features
        across different files and avoid import errors.
        It is the only file where we use imports inside
        the function. For more information about the object,
        please refer to the link above.
    """
    from verticapy.core.vdataframe.base import vDataColumn

    return vDataColumn(*args, **kwargs)


def create_new_vdf(*args, **kwargs) -> "vDataFrame":
    """
    Creates a :py:class:`vDataFrame`.

    .. note::

        This function is used to bring main features
        across different files and avoid import errors.
        It is the only file where we use imports inside
        the function. For more information about the object,
        please refer to the link above.
    """
    from verticapy.core.vdataframe.base import vDataFrame

    return vDataFrame(*args, **kwargs)


def get_vertica_mllib() -> Literal["vml"]:
    """
    Gets the Vertica machine learning module:
    :py:mod:`verticapy.machine_learning.vertica`.

    .. note::

        This function is used to bring main features
        across different files and avoid import errors.
        It is the only file where we use imports inside
        the function. For more information about the object,
        please refer to the link above.
    """
    import verticapy.machine_learning.vertica as vml

    return vml


def read_pd(*args, **kwargs) -> "vDataFrame":
    """
    Reads a Pandas DataFrame into a VerticaPy
    vDataFrame. It uses the
    :py:func:`verticapy.pandas.read_pandas`
    function.

    .. note::

        This function is used to bring main features
        across different files and avoid import errors.
        It is the only file where we use imports inside
        the function. For more information about the object,
        please refer to the link above.
    """
    from verticapy.core.parsers.pandas import read_pandas

    return read_pandas(*args, **kwargs)
