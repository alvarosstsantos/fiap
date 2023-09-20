import pycountry

# country name alternatives that can't be found on pycountry dict
a = {
    "Netherlands Antilles": "ANT",
    "Russia": "RUS",
    "Cape Verde": "CPV",
    "Democratic Republic of the Congo":"COD",
    "São Tome and Principe":"STP",
    "Bahrein": "BHR",
    "Iran": "IRN",
    "Dominica Island": "DMA",
    "French Guyana": "GUF",
    "Saint Vicent and the Granadines": "VCT",
    "Swaziland": "SWZ",
    "Saint Christopher and Nevis": "KNA"
}

def alpha_3_code(country_name: str) -> str or None:
    """Convert country name to alpha 3 code."""
    c = None

    for y in (
        lambda x: pycountry.countries.get(name=x).alpha_3,
        lambda x: pycountry.countries.get(common_name=x).alpha_3,
        lambda x: pycountry.countries.get(official_name=x).alpha_3,
        lambda x: a[x]
    ):
        try:
            c = y(country_name)
        except:
            continue
        break

    return c