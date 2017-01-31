# -*- coding: utf-8 -*-
from fatcatmap.pipelines import AppPipeline


## DataPipeline - parent to all analysis/materialized data pipelines
class DataPipeline(AppPipeline):

    ''' Abstract parent class for low-level data analysis/materialization pipelines. '''

    pass
