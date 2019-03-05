def parse_metadata(request):
    meta = request.META
    cf_connecting_ip = meta.get('HTTP_CF_CONNECTING_IP')
    if cf_connecting_ip is not None:
        ip = cf_connecting_ip
        user_agent = meta.get('HTTP_USER_AGENT')
        country = meta.get('HTTP_CF_IPCOUNTRY')
    else:
        x_forwarded_for = meta.get('HTTP_X_FORWARDED_FOR')
        x_geoip_country = meta.get('HTTP_X_GEOIP_COUNTRY')

        ip = x_forwarded_for.split(',')[0] if x_forwarded_for is not None else meta.get('REMOTE_ADDR')
        user_agent = meta.get('HTTP_USER_AGENT')
        country = x_geoip_country if x_geoip_country is not None and len(x_geoip_country) == 2 else None

    return {
        'ip': ip,
        'agent': user_agent,
        'country': country,
    }
