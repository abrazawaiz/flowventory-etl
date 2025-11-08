CREATE SCHEMA IF NOT EXISTS flowventory_staging;

CREATE TABLE IF NOT EXISTS flowventory_staging.stg_inventory_full (
    id SERIAL PRIMARY KEY,
    sku_id TEXT,
    sku_name TEXT,
    category TEXT,
    abc_class TEXT,
    supplier_id TEXT,
    supplier_name TEXT,
    warehouse_id TEXT,
    warehouse_location TEXT,
    batch_id TEXT,
    received_date DATE,
    last_purchase_date DATE,
    expiry_date DATE,
    stock_age_days INT,
    quantity_on_hand INT,
    quantity_reserved INT,
    quantity_committed INT,
    damaged_qty INT,
    returns_qty INT,
    avg_daily_sales FLOAT,
    forecast_next_30d FLOAT,
    days_of_inventory FLOAT,
    reorder_point FLOAT,
    safety_stock FLOAT,
    lead_time_days INT,
    unit_cost_usd FLOAT,
    last_purchase_price_usd FLOAT,
    total_inventory_value_usd FLOAT,
    sku_churn_rate FLOAT,
    order_frequency_per_month FLOAT,
    supplier_ontime_pct FLOAT,
    fifo_fefo TEXT,
    inventory_status TEXT,
    count_variance INT,
    audit_date DATE,
    audit_variance_pct FLOAT,
    demand_forecast_accuracy_pct FLOAT,
    notes TEXT,
    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_sku_id 
    ON flowventory_staging.stg_inventory_full (sku_id);

CREATE INDEX IF NOT EXISTS idx_category 
    ON flowventory_staging.stg_inventory_full (category);

CREATE INDEX IF NOT EXISTS idx_supplier 
    ON flowventory_staging.stg_inventory_full (supplier_name);

CREATE INDEX IF NOT EXISTS idx_warehouse 
    ON flowventory_staging.stg_inventory_full (warehouse_id);

CREATE INDEX IF NOT EXISTS idx_received_date 
    ON flowventory_staging.stg_inventory_full (received_date);

CREATE INDEX IF NOT EXISTS idx_expiry_date 
    ON flowventory_staging.stg_inventory_full (expiry_date);

DO $$
BEGIN
    RAISE NOTICE 'Schema flowventory_staging ready.';
    RAISE NOTICE 'Table stg_inventory_full created with 37 columns.';
END$$;
