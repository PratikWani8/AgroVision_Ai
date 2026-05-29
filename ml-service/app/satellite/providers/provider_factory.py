from app.satellite.providers.sentinel_provider import ( SentinelProvider )
from app.satellite.providers.landsat_provider import ( LandsatProvider )
from app.satellite.providers.earth_engine_provider import ( EarthEngineProvider )
from app.satellite.providers.nasa_provider import ( NASAProvider )

class ProviderFactory:

    @staticmethod
    def get_provider(
        provider_name
    ):
        providers = {
            "sentinel":
                SentinelProvider(),

            "landsat":
                LandsatProvider(),

            "earth_engine":
                EarthEngineProvider(),

            "nasa":
                NASAProvider()
        }

        provider = providers.get(
            provider_name
        )

        if not provider:
            raise Exception(
                "Invalid satellite provider"
            )

        return provider