from datetime import datetime
from app.models import AssetData
from app.models import Asset
from yahoo_finance import Share
from collections import OrderedDict


class AssetDataApi():
    def addDetails(self, prediction, errorMargin, neteffect, startDate, endDate, arimaeffect):
        date_format = "%Y-%m-%d"
        for asset in Asset.objects.all():
            symbol = asset.symbol
            historicalData = OrderedDict()
            assetInfo = []
            # Share(symbol)
            historicalData = assetInfo.get_historical(startDate, endDate)
            if len(historicalData) == 0:
                raise Exception("Yahoo API failed")
            else:
                historicalData.reverse()
                for dailyData in historicalData:
                    data = AssetData(asset=asset, errorMargin=errorMargin, prediction=prediction,
                                     price=dailyData['Close'],
                                     timestamp=datetime.strptime(dailyData['Date'], date_format), neteffect=neteffect,
                                     arimaeffect=arimaeffect)
                data.save()
