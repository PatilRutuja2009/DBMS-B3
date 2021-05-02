> db.orders1.insert({"Cust_id":"pqr222","Order_date":new Date("oct 04,2012"),"Status":"P","Price":50,"Items":[{"Sku":"115","Qty":35,"Price":350},{"Sku":"116","Qty":60,"Price":250}]})
> db.orders1.insert({"Cust_id":"pqr223","Order_date":new Date("oct 05,2016"),"Status":"A","Price":50,"Items":[{"Sku":"112","Qty":35,"Price":350},{"Sku":"111","Qty":60,"Price":350}]})
> db.orders1.insert({"Cust_id":"pqr224","Order_date":new Date("jun 27,2018"),"Status":"A","Price":350,"Items":[{"Sku":"114","Qty":35,"Price":450},{"Sku":"113","Qty":60,"Price":250}]})
> db.orders1.insert({"Cust_id":"pqr225","Order_date":new Date(""),"Status":"P","Price":100,"Items":[{"Sku":"118","Qty":35,"Price":750},{"Sku":"117","Qty":60,"Price":250}]})
> db.orders1.insert({"Cust_id":"pqr226","Order_date":new Date("may 12,2015"),"Status":"A","Price":100,"Items":[{"Toy":"119","Qty":35,"Price":150},{"Sku":"120","Qty":60,"Price":150}]})
> db.orders1.find().pretty()
{
    "_id" : ObjectId("5d91784a42ada94a497bd9db"),
    "Cust_id" : "pqr222",
    "Order_date" : ISODate("2012-10-03T18:30:00Z"),
    "Status" : "P",
    "Price" : 50,
    "Items" : [
        {
            "Sku" : "115",
            "Qty" : 35,
            "Price" : 350
        },
        {
            "Sku" : "116",
            "Qty" : 60,
            "Price" : 250
        }
    ]
}
{
    "_id" : ObjectId("5d91787042ada94a497bd9dc"),
    "Cust_id" : "pqr223",
    "Order_date" : ISODate("2016-10-04T18:30:00Z"),
    "Status" : "A",
    "Price" : 50,
    "Items" : [
        {
            "Sku" : "112",
            "Qty" : 35,
            "Price" : 350
        },
        {
            "Sku" : "111",
            "Qty" : 60,
            "Price" : 350
        }
    ]
}
{
    "_id" : ObjectId("5d91789d42ada94a497bd9dd"),
    "Cust_id" : "pqr224",
    "Order_date" : ISODate("2018-06-26T18:30:00Z"),
    "Status" : "A",
    "Price" : 350,
    "Items" : [
        {
            "Sku" : "114",
            "Qty" : 35,
            "Price" : 450
        },
        {
            "Sku" : "113",
            "Qty" : 60,
            "Price" : 250
        }
    ]
}
{
    "_id" : ObjectId("5d9178cc42ada94a497bd9de"),
    "Cust_id" : "pqr225",
    "Order_date" : ISODate("0NaN-NaN-NaNTNaN:NaN:NaNZ"),
    "Status" : "P",
    "Price" : 100,
    "Items" : [
        {
            "Sku" : "118",
            "Qty" : 35,
            "Price" : 750
        },
        {
            "Sku" : "117",
            "Qty" : 60,
            "Price" : 250
        }
    ]
}
{
    "_id" : ObjectId("5d91792442ada94a497bd9df"),
    "Cust_id" : "pqr226",
    "Order_date" : ISODate("2015-05-11T18:30:00Z"),
    "Status" : "A",
    "Price" : 100,
    "Items" : [
        {
            "Toy" : "119",
            "Qty" : 35,
            "Price" : 150
        },
        {
            "Sku" : "120",
            "Qty" : 60,
            "Price" : 150
        }
    ]
}
> db.orders1.count()
5
> db.orders1.aggregate([{$group:{_id:"Cust_id",Total:{$sum:"$Price"}}}])
{ "result" : [ { "_id" : "Cust_id", "Total" : 1050 } ], "ok" : 1 }
> db.orders1.aggregate([{$group:{_id:"$Cust_id",Total:{$sum:"$Price"}}}])
{
    "result" : [
        {
            "_id" : "pqr226",
            "Total" : 500
        },
        {
            "_id" : "pqr225",
            "Total" : 100
        },
        {
            "_id" : "pqr224",
            "Total" : 350
        },
        {
            "_id" : "pqr223",
            "Total" : 50
        },
        {
            "_id" : "pqr222",
            "Total" : 50
        }
    ],
    "ok" : 1
}
> db.orders1.aggregate([{$group:{_id:"$Cust_id",Total:{$sum:"$Price"}}},{$sort:{Total:1}}])
{
    "result" : [
        {
            "_id" : "pqr223",
            "Total" : 50
        },
        {
            "_id" : "pqr222",
            "Total" : 50
        },
        {
            "_id" : "pqr225",
            "Total" : 100
        },
        {
            "_id" : "pqr224",
            "Total" : 350
        },
        {
            "_id" : "pqr226",
            "Total" : 500
        }
    ],
    "ok" : 1
}
> db.orders1.aggregate([{$group:{_id:"$Cust_id",Total:{$sum:"$Price"}}},{$sort:{Total:-1}}])
{
    "result" : [
        {
            "_id" : "pqr226",
            "Total" : 500
        },
        {
            "_id" : "pqr224",
            "Total" : 350
        },
        {
            "_id" : "pqr225",
            "Total" : 100
        },
        {
            "_id" : "pqr223",
            "Total" : 50
        },
        {
            "_id" : "pqr222",
            "Total" : 50
        }
    ],
    "ok" : 1
}
> db.orders1.aggregate([{$group:{_id:"$Order_date",Total:{$sum:"$Price"}}},{$sort:{Total:-1}}])
{
    "result" : [
        {
            "_id" : ISODate("0NaN-NaN-NaNTNaN:NaN:NaNZ"),
            "Total" : 400
        },
        {
            "_id" : ISODate("2018-06-26T18:30:00Z"),
            "Total" : 350
        },
        {
            "_id" : ISODate("2015-05-23T03:44:56Z"),
            "Total" : 100
        },
        {
            "_id" : ISODate("2015-05-11T18:30:00Z"),
            "Total" : 100
        },
        {
            "_id" : ISODate("2016-10-04T18:30:00Z"),
            "Total" : 50
        },
        {
            "_id" : ISODate("2012-10-03T18:30:00Z"),
            "Total" : 50
        }
    ],
    "ok" : 1
}
> db.orders1.aggregate([{$group:{_id:"$Order_date",Total:{$sum:"$Price"}}}])
{
    "result" : [
        {
            "_id" : ISODate("2015-05-23T03:44:56Z"),
            "Total" : 100
        },
        {
            "_id" : ISODate("2015-05-11T18:30:00Z"),
            "Total" : 100
        },
        {
            "_id" : ISODate("0NaN-NaN-NaNTNaN:NaN:NaNZ"),
            "Total" : 400
        },
        {
            "_id" : ISODate("2018-06-26T18:30:00Z"),
            "Total" : 350
        },
        {
            "_id" : ISODate("2016-10-04T18:30:00Z"),
            "Total" : 50
        },
        {
            "_id" : ISODate("2012-10-03T18:30:00Z"),
            "Total" : 50
        }
    ],
    "ok" : 1
}
> db.orders1.aggregate([{$group:{_id:"$Cust_id",count:{$sum:1}}}])
{
    "result" : [
        {
            "_id" : "pqr226",
            "count" : 5
        },
        {
            "_id" : "pqr225",
            "count" : 1
        },
        {
            "_id" : "pqr224",
            "count" : 1
        },
        {
            "_id" : "pqr223",
            "count" : 1
        },
        {
            "_id" : "pqr222",
            "count" : 1
        }
    ],
    "ok" : 1
}
> db.orders1.aggregate([{$group:{_id:"$Order_date",Total:{$sum:"$Price"}}},{$match:{Total:{$gt:250}}}])
{
    "result" : [
        {
            "_id" : ISODate("0NaN-NaN-NaNTNaN:NaN:NaNZ"),
            "Total" : 400
        },
        {
            "_id" : ISODate("2018-06-26T18:30:00Z"),
            "Total" : 350
        }
    ],
    "ok" : 1
}

> db.orders1.aggregate([{$match:{Status:"A"}},{$group:{_id:"$Cust_id",Total:{$sum:"$Price"}}}])
{
    "result" : [
        {
            "_id" : "pqr226",
            "Total" : 500
        },
        {
            "_id" : "pqr224",
            "Total" : 350
        },
        {
            "_id" : "pqr223",
            "Total" : 50
        }
    ],
    "ok" : 1
}
