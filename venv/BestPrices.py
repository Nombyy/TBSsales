import re
# fully load a sale page in TBS (expand all the load more options), right click on the page and save as html
filename = "../Webpages/gifts.html"
myFile = open(filename, "rb")

# regex expressions to parse for
pname = '<h3 class="product-title" itemprop="name" aria-describedby=".+"> (.+)<\/h3>'
before = 'Previous price was \$([0-9]+(\.[0-9][0-9])?)'
after = 'Current price is  \$([0-9]+(\.[0-9][0-9])?)'

# Declare flags for if they are found to be false; somewhat of a hack for now
gn = False
bn = False
an = False
sale = None
found = None
items = []

for line in myFile:
    # Have to decode the binary file lines first
    line = line.decode('UTF-8')
    found = re.search(pname, line)
    if found:
        gn = found.group(1)
    if not an:
        found = re.search(after, line)
        if found:
            an = found.group(1)
    elif not bn:
        found = re.search(before, line)
        if found:
            bn = found.group(1)
            sale = "{0:.2f}".format(float(an) / float(bn) * 100)
            listing = str(sale) + '% ' + gn + ' was:' + bn + ' now:' + an
            items.append(listing)
            gn = False
            bn = False
            an = False

items.sort()
for i in items:
    print(i)