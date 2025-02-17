.. _chart_gallery.pivot:

===========
Pivot Table
===========

.. Necessary Code Elements

.. ipython:: python
    :suppress:

    import verticapy as vp

    N = 100 # Number of records

    data = vp.vDataFrame({
        "category1": [np.random.choice(['A','B','C']) for _ in range(N)],
        "category2": [np.random.choice(['D','E']) for _ in range(N)],
        "score1": np.random.normal(10, 2, N),
        "score2": np.random.normal(5, 1.5, N),
    })


General
-------

Let's begin by importing `VerticaPy`.

.. ipython:: python

    import verticapy as vp

Let's also import `numpy` to create a random dataset.

.. ipython:: python

    import numpy as np

Let's generate a dataset using the following data.

.. code-block:: python
        
    N = 100 # Number of records

    data = vp.vDataFrame({
        "category1": [np.random.choice(['A','B','C']) for _ in range(N)],
        "category2": [np.random.choice(['D','E']) for _ in range(N)],
        "score1": np.random.normal(10, 2, N),
        "score2": np.random.normal(5, 1.5, N),
    })

In the context of data visualization, we have the flexibility to harness multiple plotting libraries to craft a wide range of graphical representations. VerticaPy, as a versatile tool, provides support for several graphic libraries, such as Matplotlib, Highcharts, and Plotly. Each of these libraries offers unique features and capabilities, allowing us to choose the most suitable one for our specific data visualization needs.

.. image:: ../../docs/source/_static/plotting_libs.png
   :width: 80%
   :align: center

.. note::
    
    To select the desired plotting library, we simply need to use the `set_option` function. VerticaPy offers the flexibility to smoothly transition between different plotting libraries. In instances where a particular graphic is not supported by the chosen library or is not supported within the VerticaPy framework, the tool will automatically generate a warning and then switch to an alternative library where the graphic can be created.

Please click on the tabs to view the various graphics generated by the different plotting libraries.

.. ipython:: python
    :suppress:

    import verticapy as vp

.. tab:: Plotly

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "plotly")

    We can switch to using the `plotly` module.

    .. code-block:: python
        
        vp.set_option("plotting_lib", "plotly")

    VerticaPy has the capability to calculate comprehensive pivot tables and can also automatically discretize and group numerical features, simplifying the data analysis process.
    
    .. tab:: Pivot

      .. tab:: Python

        .. code-block:: python
          
            data.pivot_table(columns = ["category1", "category2"])

      .. tab:: SQL

        We load the VerticaPy `chart` extension.

        .. code-block:: python

            %load_ext verticapy.chart

        We write the SQL query using Jupyter magic cells.

        .. code-block:: sql
            
            %%chart -k spider
            SELECT category1, category2, COUNT(*) FROM :data GROUP BY 1, 2;

      .. ipython:: python
          :suppress:
        
          fig = data.pivot_table(columns = ["category1", "category2"], width = 650)
          fig.write_html("figures/plotting_plotly_pivot.html")

      .. raw:: html
          :file: SPHINX_DIRECTORY/figures/plotting_plotly_pivot.html

.. tab:: Highcharts

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "highcharts")

    We can switch to using the `highcharts` module.

    .. code-block:: python
        
        vp.set_option("plotting_lib", "highcharts")

    VerticaPy has the capability to calculate comprehensive pivot tables and can also automatically discretize and group numerical features, simplifying the data analysis process.

    .. tab:: Pivot

      .. tab:: Python

        .. code-block:: python
          
            data.pivot_table(columns = ["category1", "category2"])

      .. tab:: SQL

        We load the VerticaPy `chart` extension.

        .. code-block:: python

            %load_ext verticapy.chart

        We write the SQL query using Jupyter magic cells.

        .. code-block:: sql
            
            %%chart -k spider
            SELECT category1, category2, COUNT(*) FROM :data GROUP BY 1, 2;

      .. ipython:: python
          :suppress:

          fig = data.pivot_table(columns = ["category1", "category2"])
          html_text = fig.htmlcontent.replace("container", "plotting_highcharts_pivot")
          with open("figures/plotting_highcharts_pivot.html", "w") as file:
            file.write(html_text)

      .. raw:: html
          :file: SPHINX_DIRECTORY/figures/plotting_highcharts_pivot.html
        
.. tab:: Matplotlib

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "matplotlib")

    We can switch to using the `matplotlib` module.

    .. code-block:: python
        
        vp.set_option("plotting_lib", "matplotlib")

    VerticaPy has the capability to calculate comprehensive pivot tables and can also automatically discretize and group numerical features, simplifying the data analysis process.

    .. tab:: Pivot

      .. tab:: Python

        .. ipython:: python
            :okwarning:
          
            @savefig plotting_matplotlib_pivot.png
            data.pivot_table(columns = ["category1", "category2"])

      .. tab:: SQL

        We load the VerticaPy `chart` extension.

        .. code-block:: python

            %load_ext verticapy.chart

        We write the SQL query using Jupyter magic cells.

        .. code-block:: sql
            
            %%chart -k spider
            SELECT category1, category2, COUNT(*) FROM :data GROUP BY 1, 2;

        .. image:: ../../docs/source/savefig/plotting_matplotlib_pivot.png
            :width: 100%
            :align: center
        
    .. tab:: Hexbin

      .. ipython:: python
          :okwarning:

          @savefig plotting_matplotlib_hexbin.png
          data.hexbin(columns = ["score1", "score2"])

___________________

Custom Aggregations
-------------------

Within the VerticaPy framework, you have the flexibility to apply a wide array of aggregation techniques according to your specific analytical needs. This extends to the option of utilizing SQL statements, allowing you to craft custom aggregations that precisely match your data summarization requirements. VerticaPy empowers you with the versatility to aggregate data in the manner that best serves your analytical objectives.

.. note::

    In SQL, aggregations can be computed directly within the input SQL statement, but in Python, the process is a bit different.

.. tab:: Plotly

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib","plotly")

    **General Options**

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"], method = "count", of = "score1")

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], method = "count", of = "score1", width = 650)
        fig.write_html("figures/plotting_plotly_pivot_custom_agg_1.html")

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_plotly_pivot_custom_agg_1.html

    .. hint:: VerticaPy simplifies the usage of aggregations, such as percentiles. You only need to specify the percentile number without a decimal point to compute it. For instance, 50% for the median, 75% for the third quartile, and 99% for the last percentile.

    **Direct SQL statement**

    .. note:: You are free to utilize any SQL statement as long as it is compatible with the supported features of VerticaPy.

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"], method = "COUNT(score1) AS count_score")

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], method = "COUNT(score1) AS count_score", width = 650)
        fig.write_html("figures/plotting_plotly_pivot_custom_agg_2.html")

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_plotly_pivot_custom_agg_2.html

.. tab:: Highcharts

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "highcharts")

    **General Options**

    .. code-block:: python
              
        data.pivot_table(columns = ["category1", "category2"], method = "min", of = "score1")

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], method = "min", of = "score1")
        html_text = fig.htmlcontent.replace("container", "plotting_highcharts_pivot_custom_agg_1")
        with open("figures/plotting_highcharts_pivot_custom_agg_1.html", "w") as file:
          file.write(html_text)

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_highcharts_pivot_custom_agg_1.html

    .. hint:: VerticaPy simplifies the usage of aggregations, such as percentiles. You only need to specify the percentile number without a decimal point to compute it. For instance, 50% for the median, 75% for the third quartile, and 99% for the last percentile.

    **Direct SQL statement**

    .. note:: You are free to utilize any SQL statement as long as it is compatible with the supported features of VerticaPy.

    .. code-block:: python
              
        data.pivot_table(columns = ["category1", "category2"], method = "MIN(score1) AS min_score")

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], method = "MIN(score1) AS min_score")
        html_text = fig.htmlcontent.replace("container", "plotting_highcharts_pivot_custom_agg_2")
        with open("figures/plotting_highcharts_pivot_custom_agg_2.html", "w") as file:
          file.write(html_text)

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_highcharts_pivot_custom_agg_2.html

.. tab:: Matplolib

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "matplotlib")

    **General Options**

    .. ipython:: python
        :okwarning:

        @savefig plotting_matplotlib_pivot_custom_agg_1.png
        data.pivot_table(columns = ["category1", "category2"], method = "min", of = "score1")

    .. hint:: VerticaPy simplifies the usage of aggregations, such as percentiles. You only need to specify the percentile number without a decimal point to compute it. For instance, 50% for the median, 75% for the third quartile, and 99% for the last percentile.

    **Direct SQL statement**

    .. note:: You are free to utilize any SQL statement as long as it is compatible with the supported features of VerticaPy.

    .. ipython:: python
        :okwarning:

        @savefig plotting_matplotlib_pivot_custom_agg_2.png
        data.pivot_table(columns = ["category1", "category2"], method = "MIN(score1) AS min_score")

___________________


Chart Customization
-------------------

VerticaPy empowers users with a high degree of flexibility when it comes to tailoring the visual aspects of their plots. 
This customization extends to essential elements such as **color schemes**, **text labels**, and **plot sizes**, as well as a wide range of other attributes that can be fine-tuned to align with specific design preferences and analytical requirements. Whether you want to make your visualizations more visually appealing or need to convey specific insights with precision, VerticaPy's customization options enable you to craft graphics that suit your exact needs.

.. hint::

    For SQL users who use Jupyter Magic cells, chart customization must be done in Python. They can then export the graphic using the last magic cell result.

    .. code-block:: python

        chart = _

    Now, the chart variable includes the graphic. Depending on the library you are using, you will obtain a different object.

.. Important:: Different customization parameters are available for Plotly, Highcharts, and Matplotlib. 
    For a comprehensive list of customization features, please consult the documentation of the respective 
    libraries: `plotly <https://plotly.com/python-api-reference/>`_, `matplotlib <https://matplotlib.org/stable/api/matplotlib_configuration_api.html>`_ and `highcharts <https://api.highcharts.com/highcharts/>`_.

Colors
~~~~~~

.. tab:: Plotly

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "plotly")

    **Custom CMAP**

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"], color_continuous_scale = [[0, "white"], [1, "red"]])

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], color_continuous_scale = [[0, "white"], [1, "red"]], width = 650)
        fig.write_html("figures/plotting_plotly_pivot_custom_color_1.html")

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_plotly_pivot_custom_color_1.html

.. tab:: Highcharts

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "highcharts")

    **Custom CMAP**

    .. code-block:: python
        
        fig = data.pivot_table(columns = ["category1", "category2"])
        fig.set_options(
            "colorAxis",
            {
                "stops": [
                    [0, "white"],
                    [0.45, "yellow"],
                    [0.55, "pink"],
                    [1, "red"],
                ],
                "min": -1,
                "max": 1,
            },
        )
        fig

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"])
        fig.set_options(
            "colorAxis",
            {
                "stops": [
                    [0, "white"],
                    [0.45, "yellow"],
                    [0.55, "pink"],
                    [1, "red"],
                ],
                "min": -1,
                "max": 1,
            },
        )
        html_text = fig.htmlcontent.replace("container", "plotting_highcharts_pivot_custom_color_1")
        with open("figures/plotting_highcharts_pivot_custom_color_1.html", "w") as file:
            file.write(html_text)

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_highcharts_pivot_custom_color_1.html

.. tab:: Matplolib

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "matplotlib")

    **Custom CMAP**

    .. ipython:: python
        :okwarning:

        @savefig plotting_matplotlib_pivot_custom_color_1.png
        data.pivot_table(columns = ["category1", "category2"], cmap = "Reds")

____

Size
~~~~

.. tab:: Plotly

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "plotly")

    **Custom Width and Height**

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"], width = 300, height = 300)

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], width = 300, height = 300)
        fig.write_html("figures/plotting_plotly_pivot_custom_size.html")

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_plotly_pivot_custom_size.html

.. tab:: Highcharts

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "highcharts")

    **Custom Width and Height**

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"], width = 500, height = 200)

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], width = 500, height = 200)
        html_text = fig.htmlcontent.replace("container", "plotting_highcharts_pivot_custom_size")
        with open("figures/plotting_highcharts_pivot_custom_size.html", "w") as file:
            file.write(html_text)

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_highcharts_pivot_custom_size.html

.. tab:: Matplolib

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "matplotlib")

    **Custom Width and Height**

    .. ipython:: python
        :okwarning:

        @savefig plotting_matplotlib_pivot_custom_size.png
        data.pivot_table(columns = ["category1", "category2"], width = 6, height = 3)

_____


Text
~~~~

.. tab:: Plotly

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "plotly")

    **Custom Title**

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"]).update_layout(title_text = "Custom Title")

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], width = 650).update_layout(title_text = "Custom Title")
        fig.write_html("figures/plotting_plotly_pivot_custom_main_title.html")

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_plotly_pivot_custom_main_title.html

    **Custom Axis Titles**

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"], yaxis_title = "Custom Y-Axis Title")

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], yaxis_title = "Custom Y-Axis Title", width = 650)
        fig.write_html("figures/plotting_plotly_pivot_custom_y_title.html")

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_plotly_pivot_custom_y_title.html

.. tab:: Highcharts

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "highcharts")

    **Custom Title Text**

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"], title = {"text": "Custom Title"})

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], title = {"text": "Custom Title"})
        html_text = fig.htmlcontent.replace("container", "plotting_highcharts_pivot_custom_text_title")
        with open("figures/plotting_highcharts_pivot_custom_text_title.html", "w") as file:
            file.write(html_text)

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_highcharts_pivot_custom_text_title.html

    **Custom Axis Titles**

    .. code-block:: python
        
        data.pivot_table(columns = ["category1", "category2"], xAxis = {"title": {"text": "Custom X-Axis Title"}})

    .. ipython:: python
        :suppress:

        fig = data.pivot_table(columns = ["category1", "category2"], xAxis = {"title": {"text": "Custom X-Axis Title"}})
        html_text = fig.htmlcontent.replace("container", "plotting_highcharts_pivot_custom_text_xtitle")
        with open("figures/plotting_highcharts_pivot_custom_text_xtitle.html", "w") as file:
            file.write(html_text)

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/plotting_highcharts_pivot_custom_text_xtitle.html

.. tab:: Matplolib

    .. ipython:: python
        :suppress:

        vp.set_option("plotting_lib", "matplotlib")

    **Custom Title Text**

    .. ipython:: python
        :okwarning:

        @savefig plotting_matplotlib_pivot_custom_title_label.png
        data.pivot_table(columns = ["category1", "category2"]).set_title("Custom Title")

    **Custom Axis Titles**

    .. ipython:: python
        :okwarning:

        @savefig plotting_matplotlib_pivot_custom_xaxis_label.png
        data.pivot_table(columns = ["category1", "category2"]).set_xlabel("Custom X Axis")

_____

