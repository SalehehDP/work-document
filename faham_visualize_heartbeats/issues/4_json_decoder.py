"""
error is : 

Traceback (most recent call last):
  File "/home/saleheh/.cache/pypoetry/virtualenvs/faham-visualize-heartbeats-RKAT3EoX-py3.10/lib/python3.10/site-packages/flask/app.py", line 2525, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/saleheh/.cache/pypoetry/virtualenvs/faham-visualize-heartbeats-RKAT3EoX-py3.10/lib/python3.10/site-packages/flask/app.py", line 1822, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/saleheh/.cache/pypoetry/virtualenvs/faham-visualize-heartbeats-RKAT3EoX-py3.10/lib/python3.10/site-packages/flask/app.py", line 1820, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/saleheh/.cache/pypoetry/virtualenvs/faham-visualize-heartbeats-RKAT3EoX-py3.10/lib/python3.10/site-packages/flask/app.py", line 1796, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
  File "/home/saleheh/.cache/pypoetry/virtualenvs/faham-visualize-heartbeats-RKAT3EoX-py3.10/lib/python3.10/site-packages/dash_auth/basic_auth.py", line 33, in wrap
    response = f(*args, **kwargs)
  File "/home/saleheh/.cache/pypoetry/virtualenvs/faham-visualize-heartbeats-RKAT3EoX-py3.10/lib/python3.10/site-packages/dash/dash.py", line 1274, in dispatch
    ctx.run(
  File "/home/saleheh/.cache/pypoetry/virtualenvs/faham-visualize-heartbeats-RKAT3EoX-py3.10/lib/python3.10/site-packages/dash/_callback.py", line 440, in add_context
    output_value = func(*func_args, **func_kwargs)  # %% callback invoked %%
  File "/home/saleheh/Documents/SIRCO/faham/faham_visualization/faham_visualize_heartbeats/src/main/faham/visualization/heartbeat/api/pages/dashboardPage.py", line 684, in update_line_chart_modam
    energy = dashboard_page.createRondomEnerge(ramz_rayane)
  File "/home/saleheh/Documents/SIRCO/faham/faham_visualization/faham_visualize_heartbeats/src/main/faham/visualization/heartbeat/api/pages/dashboardPage.py", line 345, in createRondomEnerge
    meterData = self.readMutableData("meterData")
  File "/home/saleheh/Documents/SIRCO/faham/faham_visualization/faham_visualize_heartbeats/src/main/faham/visualization/heartbeat/api/pages/dashboardPage.py", line 331, in readMutableData
    contents = json.loads(j.read())[name]
  File "/usr/lib/python3.10/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.10/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.10/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    """
