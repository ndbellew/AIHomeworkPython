
from pandas import DataFrame, concat
from pyexcel import save_as



def ToODS(timelist, name="output"):
    output = DataFrame(timelist)
    columns = ['problem', 'bfs', 'dfs', 'ids', 'bds', 'path']
    output = output.reindex(columns=columns)
    output.to_excel(name, engine='odf', index=False)