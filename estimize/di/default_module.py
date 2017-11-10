from injector import Module, singleton

from estimize.services import (
    AssetService, AssetInfoService, CacheService, CalendarService, CsvDataService, EstimizeConsensusService,
    ResidualReturnsService
)
from estimize.services.impl import (
    AssetInfoServiceDefaultImpl, CacheServiceDefaultImpl, EstimizeConsensusServiceDefaultImpl,
    ResidualReturnsServiceDefaultImpl
)
from estimize.services.impl.zipline import (
    Config, YahooConfig, AssetServiceZiplineImpl, CalendarServiceZiplineImpl, CsvDataServiceZiplineImpl
)


class DefaultModule(Module):

    def configure(self, binder):
        binder.bind(Config, to=Config, scope=singleton)
        binder.bind(YahooConfig, to=YahooConfig, scope=singleton)
        binder.bind(AssetService, to=AssetServiceZiplineImpl, scope=singleton)
        binder.bind(AssetInfoService, to=AssetInfoServiceDefaultImpl, scope=singleton)
        binder.bind(CacheService, to=CacheServiceDefaultImpl, scope=singleton)
        binder.bind(CalendarService, to=CalendarServiceZiplineImpl, scope=singleton)
        binder.bind(CsvDataService, to=CsvDataServiceZiplineImpl, scope=singleton)
        binder.bind(EstimizeConsensusService, to=EstimizeConsensusServiceDefaultImpl, scope=singleton)
        binder.bind(ResidualReturnsService, to=ResidualReturnsServiceDefaultImpl, scope=singleton)
