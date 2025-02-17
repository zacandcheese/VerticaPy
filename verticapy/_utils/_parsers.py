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
"""
import warnings

from verticapy._utils._sql._format import list_strip


def get_header_names(path: str, sep: str) -> list[str]:
    """
    Returns the input CSV file's
    header columns' names.

    Parameters
    ----------
    path: str
        File's path.
    sep: str
        CSV separator.

    Returns
    -------
    list
        header columns' names.

    Examples
    --------
    The following code demonstrates
    the usage of the function.

    .. ipython:: python

        # Import the function.
        from verticapy._utils._parsers import get_header_names

        # Creating a CSV example.
        file_name = 'verticapy_test_parsers.csv'
        f = open(file_name, 'a')
        f.write("A;B;C;D")
        f.close()

        # Example.
        get_header_names(file_name, sep = ';')

        # Deleting the CSV file.
        import os

        os.remove(file_name)

    .. note::

        These functions serve as utilities to
        construct others, simplifying the overall
        code.
    """
    with open(path, "r", encoding="utf-8") as f:
        file_header = f.readline().replace("\n", "").replace('"', "")
        if not sep:
            sep = guess_sep(file_header)
        file_header = file_header.split(sep)
    for idx, col in enumerate(file_header):
        if col == "":
            if idx == 0:
                position = "beginning"
            elif idx == len(file_header) - 1:
                position = "end"
            else:
                position = "middle"
            file_header[idx] = f"col{idx}"
            warning_message = (
                f"An inconsistent name was found in the {position} of the "
                "file header (isolated separator). It will be replaced "
                f"by col{idx}."
            )
            if idx == 0:
                warning_message += (
                    "\nThis can happen when exporting a pandas DataFrame "
                    "to CSV while retaining its indexes.\nTip: Use "
                    "index=False when exporting with pandas.DataFrame.to_csv."
                )
            warnings.warn(warning_message, Warning)
    return list_strip(file_header)


def guess_sep(file_str: str) -> str:
    """
    Guesses the file's separator.

    Parameters
    ----------
    file_str: str
        Any lines of the CSV file.

    Returns
    -------
    str
        the separator.

    Examples
    --------
    The following code demonstrates
    the usage of the function.

    .. ipython:: python

        # Import the function.
        from verticapy._utils._parsers import guess_sep

        # ',' separator.
        guess_sep('col1, col2,col3,  col4')

        # ';' separator.
        guess_sep('col1; col2;col3;  col4')

    .. note::

        These functions serve as utilities to
        construct others, simplifying the overall
        code.
    """
    sep = ","
    max_occur = file_str.count(",")
    for s in ("|", ";"):
        total_occurences = file_str.count(s)
        if total_occurences > max_occur:
            max_occur = total_occurences
            sep = s
    return sep
