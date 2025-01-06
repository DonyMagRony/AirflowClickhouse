CREATE TABLE clients (
    client_id UInt32,
    name String,
    region String
) ENGINE = MergeTree()
ORDER BY client_id;

CREATE TABLE products (
    product_id UInt32,
    name String,
    category String
) ENGINE = MergeTree()
ORDER BY product_id;

CREATE TABLE orders (
    order_id UInt32,
    client_id UInt32,
    product_id UInt32,
    order_date Date,
    total_amount UInt32
) ENGINE = MergeTree()
ORDER BY order_id;

CREATE TABLE discounts (
    product_id UInt32,
    discount_percent UInt8,
    start_date Date,
    end_date Date
) ENGINE = MergeTree()
ORDER BY product_id;
