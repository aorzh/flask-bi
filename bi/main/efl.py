import matplotlib.pyplot as plt
import numpy as np
from pandas import date_range, Series, DataFrame, read_csv, qcut, merge, concat, TimeGrouper, to_datetime, DatetimeIndex, pivot_table
import seaborn
from sqlalchemy import create_engine, MetaData, Table, schema, Integer, Numeric, String, Text, BLOB, desc
from bi.config import Config
import phpserialize


def prepare_data():
    src_engine = create_engine("mysql://root:root@localhost:5000/arik.dev")
    src_metadata = MetaData(bind=src_engine)
    src_table = Table('commerce_order', src_metadata, autoload=True)

    # engine for work
    target_engine = create_engine("mysql://root:root@localhost:5000/bi3")
    target_metadata = MetaData(bind=target_engine)
    target_table = Table('arik_orders3', target_metadata, autoload=False, extend_existing=True)

    col = schema.Column('id', Integer, primary_key=True)
    target_table.append_column(col)

    type_map = {"integer": Integer,
                "float": Numeric,
                "string": String(256),
                "text": Text,
                "date": Text,
                "boolean": Integer,
                "blob": BLOB}

    fields = [("oid", "integer"),
              ("uid", "integer"),
              ("mail", "string"),
              ("status", "string"),
              ("changed", "integer"),
              ("depart", "string"),
              ("arrive", "string")]

    field_names = []

    for (field_name, field_type) in fields:
        col = schema.Column(field_name, type_map[field_type.lower()])
        target_table.append_column(col)
        field_names.append(field_name)

    target_table.create(checkfirst=True)

    for row in src_table.select().order_by(desc("changed")).execute():
        """
        need normal mapping here!
        """
        record = (row[0], row[4], row[5], row[6], row[8])
        origin = ''
        destination = ''

        if isinstance(row[10], bytes):
            obj = phpserialize.loads(row[10])
            if bool(obj) is not False and b'segments' in obj:
                if b'origin' in obj[b'segments'][0]:
                    origin = obj[b'segments'][0][b'origin'].decode('UTF-8')
                if b'departureLocation' in obj[b'segments'][0]:
                    origin = obj[b'segments'][0][b'departureLocation'].decode('UTF-8')

                if b'destination' in obj[b'segments'][0]:
                    destination = obj[b'segments'][0][b'destination'].decode('UTF-8')

                if b'arrivalLocation' in obj[b'segments'][0]:
                    destination = obj[b'segments'][0][b'arrivalLocation'].decode('UTF-8')

                record = record + (
                    origin,
                    destination,)

        records = dict(zip(field_names, record))
        insert_command = target_table.insert()
        insert_command.execute(records)


def top20():
    # seaborn.set()
    data = read_csv(Config.STATIC + "/bi3.csv")
    """
    table = data.groupby('depart').size().sort_values(inplace=False, ascending=False)
    table2 = data.groupby('arrive').size().sort_values(inplace=False, ascending=False)
    depart = DataFrame(data, columns=['id', 'depart'])
    arrive = DataFrame(data, columns=['id', 'arrive'])
    """
    depart_arrive = DataFrame(data, columns=['id', 'depart', 'arrive'])
    g = depart_arrive.groupby(['depart', 'arrive']).count().nlargest(20, 'id')
    print(g)
    # g.plot(kind='bar')
    # print(g.to_html())
    # plt.show()
    # print(g.to_dict()['id'])

    return g

"""
if __name__ == '__main__':
    import sys
    sys.exit(main())
"""