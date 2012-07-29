# -*- coding: utf-8 -*-
from fatcatmap.pipelines import AppPipeline


## FetchPipeline - parent to all analysis/materialized data pipelines
class FetchPipeline(AppPipeline):

    ''' Abstract parent class for low-level data analysis/materialization pipelines. '''

    pass
