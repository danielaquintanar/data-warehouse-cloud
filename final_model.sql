-- Crear una tabla de hechos para las ventas
create table {{ ref('fact_sales') }} as (
    select
        product_id,
        sum(quantity) as total_quantity,
        sum(price) as total_sales,
        sum(quantity * price) as total_revenue
    from {{ ref('raw_sales_data') }}
    group by product_id
);

-- Crear una tabla de dimensiones para los productos
create table {{ ref('dim_product') }} as (
    select
        product_id,
        product_name,
        category
    from {{ ref('raw_product_data') }}
);
