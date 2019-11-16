def string(tofind, englobber):
    if any(tofind in s for s in englobber): return True
    else: return False
