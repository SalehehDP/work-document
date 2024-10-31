"""

    unsupported operand type(s) for -: 'str' and 'datetime.datetime'    
    باید رشته به دیت تایم تبدیل شود و سپس مقایسه شود 
    """
"""
    Alerts :  پیام های برای اطلاع رسانی در یک باکس ایجاد می شود 


    resurses : https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/

    """

# basic Alert
dbc.Alert(
    "alert-massege",
    id="alert-id",
    dismissable=True,  # امکان بستن
    is_open=True,
    duration=4000,  # بعد از ۴ ثانیه بسته خواهد شد
),

"""
    Alerts 
    به صورت های پیشرفته تری نیز استفاده شوند و شامل بخش های برای دریافت ورودی و خروجی نیز باشند . 
    """

dbc.Alert(
    [
        html.H4("Well done!", className="alert-heading"),
        html.P(
            "This is a success alert with loads of extra text in it. So much "
            "that you can see how spacing within an alert works with this "
            "kind of content."
        ),
        html.Hr(),
        html.P(
            "Let's put some more text down here, but remove the bottom margin",
            className="mb-0",
        ),
    ]
)
