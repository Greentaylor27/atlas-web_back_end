-- Listing all bands with Glam rock and ranking them by longevity
SELECT band_name FROM metal_bands WHERE style = 'Glam rock'
SELECT formed - IFNULL(split, 0) AS lifespan FROM metal_bands
ORDER BY lifespan DESC;
