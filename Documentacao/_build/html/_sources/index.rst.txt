.. Análise documentation master file, created by
   sphinx-quickstart on Sat Dec  5 21:49:37 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Módulos e Métodos para Conexão
===================================
.. automodule:: Base_de_dados_conexoes_e_limpeza.db_connection
   :members:

===================================
Exceções específicas do módulo
===================================

.. autoexception:: Base_de_dados_conexoes_e_limpeza.db_connection.invalid_server_string_format

.. autoexception:: Base_de_dados_conexoes_e_limpeza.db_connection.invalid_server_port_value

.. autoexception:: Base_de_dados_conexoes_e_limpeza.db_connection.invalid_table_name


Módulos e Métodos para Limpeza
===================================

===================================
Limpeza dos Dados covid_airport
===================================

.. autoclass:: Base_de_dados_conexoes_e_limpeza.db_cleaning.Limpador_airport
   :members:

===================================
Limpeza dos Dados fifa_players
===================================

.. autoclass:: Base_de_dados_conexoes_e_limpeza.db_cleaning.Limpador_fifa
   :members:

===================================
Exceções específicas do módulo
===================================

.. autoexception:: Base_de_dados_conexoes_e_limpeza.db_cleaning.indexes_not_found_in_dataframe


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
