# 以Astroquery套件擷取線上天文觀測資料 - 蘇羿豪

{%hackmd DR5p-QuLTwylJM8bYjJp1Q %}

> [投影片](https://hackmd.io/p/B1pDk2iAf/)

# 挑戰1: 拼接多彩銀河 
1.  [HEASARC](https://heasarc.gsfc.nasa.gov/)  X-ray 波段
2.  [Infrared Image](https://imagine.gsfc.nasa.gov/Images/objects/milkyway_infrared_full.gif) 
3.  [IRSA infrared search](https://irsa.ipac.caltech.edu/frontpage/)
4.  [Radio Image](https://imagine.gsfc.nasa.gov/Images/objects/milkyway_radio_408MHz_full.gif)
5.  [Gaia](https://gea.esac.esa.int/archive/): focus on our Milky Way.

- 影像，光譜，光變曲線都是天文領域中用來研究星體的工具。

- Astroquery：用來整合所有網路上面可以下載天文研究資料的網站。不同望遠鏡，有一樣的API。

- VizieR：用來收集分析並發表過的天文研究數據。 (catalogs)

# 挑戰2: 梅西爾搜尋手
- [梅西爾天體列表](https://zh.wikipedia.org/wiki/%E6%A2%85%E8%A5%BF%E8%80%B6%E5%A4%A9%E4%BD%93%E5%88%97%E8%A1%A8#%E5%A4%A9%E9%AB%94%E5%88%97%E8%A1%A8)
- 超新星爆炸殘骸：[Image](https://zh.wikipedia.org/wiki/%E6%A2%85%E8%A5%BF%E8%80%B6%E5%A4%A9%E4%BD%93%E5%88%97%E8%A1%A8#/media/File:Crab_Nebula.jpg)

Query an object across all catalogs
```python
from astroquery.vizier import Vizier
obj_result = Vizier.query_object("m1")

print(obj_result)
```


[使用Astroquery撈取VizieR的資料做分析](https://github.com/YihaoSu/astroquery-notes)

```python
cat_result = Vizier.get_catalogs("J/AZh/83/542/pulsars")
```

- `_RA`(赤經), `_DE`(赤緯) 欄位：用來定位天體 ([赤道座標](https://en.wikipedia.org/wiki/Equatorial_coordinate_system))


###### tags: `pycontw2018`