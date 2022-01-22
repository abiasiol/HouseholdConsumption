import nbformat

# Reading the notebooks
nb_list = ['01_time_series_analysis_import.ipynb',
           '02_time_series_analysis_data_exploration.ipynb',
           '03_time_series_decomposition.ipynb',
           '04_time_series_smoothing_prediction.ipynb',
           '05_time_series_cross_validation.ipynb'
           ]

for nb_name in nb_list:
    nb = nbformat.read(nb_name, 4)

    if nb_name == nb_list[0]:
        # Creating a new notebook
        final_notebook = nbformat.v4.new_notebook(metadata=nb.metadata)

    final_notebook.cells += nb.cells

# Saving the new notebook
nbformat.write(final_notebook, '00_summary.ipynb')
