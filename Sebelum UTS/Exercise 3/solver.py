def euler(t,h,y,dy,Func):
  d2y = Func(t,y,dy)
  y_next = y + (h * dy)
  dy_next = dy + (h * d2y)
  return (y_next, dy_next)


def cauchy_euler(params, Func):
  # initial condition
  t0 = params['t0']
  t_akhir = params['t_akhir']
  h = params['h']
  y0 = params['y0']
  dy0 = params['dy0']

  res_euler = []
  t = []
  step = int((t_akhir - t0) / h)

  for i in range(step):
    tm = (i + 1) * h
    (y_next, dy_next) = euler(tm, h, y0, dy0, Func)
    res_euler.append(y_next)
    t.append(tm)
    y0 = y_next
    dy0 = dy_next

  return(t, res_euler)
