





    with grouped_expression as (
    select
        
        
    
  
( 1=1 and percentile_cont(0.95) within group (order by price) >= 50 and percentile_cont(0.95) within group (order by price) <= 500
)
 as expression


    from AIRBNB.DEV.dim_listings_cleansed
    

),
validation_errors as (

    select
        *
    from
        grouped_expression
    where
        not(expression = true)

)

select *
from validation_errors





