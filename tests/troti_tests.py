from nose.tools import *
from troti.monitor import *

def test_itdDateTimeToDateTime():
    data = '<itdDateTime><itdDate day="20" month="2" weekday="7" year="2016"/><itdTime ap="" hour="15" minute="47"/></itdDateTime>'
    expectedResponse = '2016-02-20 15:47:00'
    assert_equal(str(itdDateTimeToDateTime(data)),expectedResponse)


def test_itdServingLineToSevingLine():
    data = '<itdServingLine code="4" direction="Linz solarCity" key="193" motType="4" number="2" realtime="0" symbol="2"><itdNoTrain name="Straßnbahn"/><motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/></itdServingLine>'
    expectedResponse = '2 Linz solarCity'
    assert_equal(str(itdServingLineToServingLine(data)),expectedResponse)


def test_itdDepartureToDeparture():
    data = '<itdDeparture area="1" countdown="132" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582"><itdDateTime><itdDate day="20" month="2" weekday="7" year="2016"/><itdTime ap="" hour="16" minute="25"/></itdDateTime><itdServingLine code="4" direction="Linz Auwiesen" key="40" motType="4" number="1" realtime="0" symbol="1"><itdNoTrain name="Straßnbahn"/><motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/></itdServingLine></itdDeparture>'
    expectedResponse = 'Linz WIFI/LINZ AG 1 Linz Auwiesen 2016-02-20 16:25:00'
    assert_equal(str(itdDepartureToDeparture(data)),expectedResponse)

def test_itdDepartureListToDeparture():
    data = '<itdDepartureList>
			<itdDeparture area="1" countdown="4" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="17"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="184" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="4" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="17"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="233" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="12" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="25"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="113" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="12" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="25"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="18" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="19" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="32"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="246" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="19" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="32"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="188" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="27" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="40"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="35" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="27" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="40"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="92" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="34" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="47"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="239" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="34" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="47"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="179" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="42" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="55"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="4" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="42" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="14" minute="55"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="112" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="49" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="2"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="221" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="49" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="2"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="213" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="57" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="10"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="121" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="57" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="10"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="36" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="64" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="17"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="197" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="64" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="17"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="268" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="72" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="25"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="73" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="72" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="25"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="60" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="79" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="32"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="264" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="79" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="32"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="169" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="87" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="40"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="46" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="87" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="40"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="88" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="94" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="47"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="273" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="94" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="47"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="202" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="102" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="55"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="12" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="102" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="15" minute="55"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="99" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="109" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="2"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="174" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="109" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="2"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="232" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="117" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="10"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="11" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="117" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="10"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="93" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="124" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="17"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="256" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="124" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="17"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="144" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="132" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="25"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="107" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="132" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="25"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="40" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="139" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="32"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz solarCity" key="193" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="139" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="32"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="284" motType="4" number="2" realtime="0" symbol="2">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01002" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="147" mapName="NAV5" platform="1" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810573">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="40"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz JKU I Universitä key="75" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="R" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
			<itdDeparture area="1" countdown="147" mapName="NAV5" platform="0" platformName="" stopID="60501200" stopName="Linz WIFI/LINZ AG" x="5448848" y="810582">
				<itdDateTime>
					<itdDate day="20" month="2" weekday="7" year="2016"/>
					<itdTime ap="" hour="16" minute="40"/>
				</itdDateTime>
				<itdServingLine code="4" direction="Linz Auwiesen" key="59" motType="4" number="1" realtime="0" symbol="1">
					<itdNoTrain name="Straßnbahn"/>
					<motDivaParams direction="H" line="01001" network="esg" project="g15" supplement="E"/>
				</itdServingLine>
			</itdDeparture>
		</itdDepartureList>'
 
