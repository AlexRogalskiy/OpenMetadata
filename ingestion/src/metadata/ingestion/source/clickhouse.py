#  Copyright 2021 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from clickhouse_sqlalchemy.drivers.base import ClickHouseDialect
from sqlalchemy.engine import reflection

from metadata.ingestion.ometa.openmetadata_rest import MetadataServerConfig
from metadata.ingestion.source.sql_source import SQLSource
from metadata.ingestion.source.sql_source_common import SQLConnectionConfig


@reflection.cache
def get_pk_constraint(self, bind, table_name, schema=None, **kw):
    return {"constrained_columns": [], "name": "undefined"}


ClickHouseDialect.get_pk_constraint = get_pk_constraint


class ClickhouseConfig(SQLConnectionConfig):
    host_port = "localhost:8123"
    scheme = "clickhouse+http"
    service_type = "ClickHouse"

    def get_connection_url(self):
        return super().get_connection_url()


class ClickhouseSource(SQLSource):
    def __init__(self, config, metadata_config, ctx):
        super().__init__(config, metadata_config, ctx)

    @classmethod
    def create(cls, config_dict, metadata_config_dict, ctx):
        config = ClickhouseConfig.parse_obj(config_dict)
        metadata_config = MetadataServerConfig.parse_obj(metadata_config_dict)
        return cls(config, metadata_config, ctx)