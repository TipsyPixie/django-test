def parse_request(request):
    meta = request.META
    cf_connecting_ip = meta.get('HTTP_CF_CONNECTING_IP')
    if cf_connecting_ip is not None:
        request_ip = cf_connecting_ip
        request_agent = meta.get('HTTP_USER_AGENT')
        request_country = meta.get('HTTP_CF_IPCOUNTRY')
    else:
        x_forwarded_for = meta.get('HTTP_X_FORWARDED_FOR')
        x_geoip_country = meta.get('HTTP_X_GEOIP_COUNTRY')
        request_ip = x_forwarded_for.split(',')[0] if x_forwarded_for is not None else meta.get('REMOTE_ADDR')
        request_agent = meta.get('HTTP_USER_AGENT')
        request_country = x_geoip_country if x_geoip_country is not None and len(x_geoip_country) == 2 else None

    return {
        'ip': request_ip,
        'agent': request_agent,
        'country': request_country,
    }
