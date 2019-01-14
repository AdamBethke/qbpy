API_AddReplaceDBPage
********************

`Quick Base Documentation: API_AddReplaceDBPage <https://help.quickbase.com/api-guide/#add_replace_dbpage.html>`_

Request
^^^^^^^

.. code:: python

    qb.api('API_AddReplaceDBPage', {
        'pagename': 'newstylesheet.xsl',
        'pagetype': 1,
        'pagebody':
            '''
            <?xml version='1.0'?>
            <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
             <xsl:template match="/">
               <html>
                <head>
                </head>
                <body>
                  Hello World
                </body>
               </html>
             </xsl:template>
            </xsl:stylesheet>
            ''',
    })

Response
^^^^^^^^

.. code:: python

    qb.response
    OrderedDict([
        ('action', 'API_AddReplaceDBPage'),
        ('errcode', 0),
        ('errtext', 'No error'),
        ('pageID', 6)
    ])
