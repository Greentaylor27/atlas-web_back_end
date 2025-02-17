-- Listing all bands with Glam rock and ranking them by longevity
SELECT band_name, IFNULL(split, 0) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
