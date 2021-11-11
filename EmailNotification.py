import yagmail


# sends email to the desired address, notifying them of what products
# have been added and taken off the site and whether products are
# now out of stock or are back in stock
def send_email(email_address, adds, subs, back_in, now_out):
    yag = yagmail.SMTP('sending email', 'password')


    separator = ', '
    additions = separator.join(adds)
    subtractions = separator.join(subs)
    back_in_stock = separator.join(back_in)
    now_out_stock = separator.join(now_out)

    if additions == "":
        additions = 'NONE'
    if subtractions == "":
        subtractions = 'NONE'
    if back_in_stock == "":
        back_in_stock = 'NONE'
    if now_out_stock == "":
        now_out_stock = 'NONE'

    email_body = f"""
    The following products have been added to the Farm Stead Website:
    {additions}
    
    The following products have been taken off the Farm Stead Website:
    {subtractions}
    
    The following products are now back in stock:
    {back_in_stock}
    
    The following products are now out of stock:
    {now_out_stock}
    
    I will now go back to sleep until next Monday, Master."""

    yag.send(to=email_address,
             subject="This Week's Farm Stead Foods Updates",
             contents=email_body)

