from django.contrib import admin

import heritagesites.models as models


@admin.register(models.Planet)
class PlanetAdmin(admin.ModelAdmin):
	fields = [
		'planet_name',
		'unsd_name'
	]

	list_display = [
		'planet_name',
		'unsd_name'
	]

@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
	fields = [
		'planet_id',
		'region_id',
		'sub_region_id',
		'intermediate_region_id'
	]

	list_display = [
		'planet_id',
		'region_id',
		'sub_region_id',
		'intermediate_region_id'
	]

	#list_filter = ['planet_id','region_id','sub_region_id']#?


@admin.register(models.CountryArea)
class CountryAreaAdmin(admin.ModelAdmin):
	fields = [
		'country_area_name',
		'iso_alpha3_code',
		'm49_code',
		'location',
		'dev_status'
	]

	list_display = [
		'country_area_name',
		'iso_alpha3_code',
		'm49_code',
		'location_id',
		'dev_status'
	]

	# list_filter = ['dev_status']

# admin.site.register(models.CountryArea)


@admin.register(models.DevStatus)
class DevStatusAdmin(admin.ModelAdmin):
	fields = ['dev_status_name']
	list_display = ['dev_status_name']
	ordering = ['dev_status_name']

# admin.site.register(models.DevStatus)


@admin.register(models.HeritageSite)
class HeritageSiteAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (
				'site_name',
				'heritage_site_category',
				'description',
				'justification',
				'date_inscribed'
			)
		}),
		('Location and Area', {
			'fields': [
				(
					'longitude',
					'latitude'
				),
				'area_hectares',
				'transboundary'
			]
		})
	)

	list_display = (
		'site_name',
		'date_inscribed',
		'area_hectares',
		'heritage_site_category',
		'country_area_display'
	)

	list_filter = (
		'heritage_site_category',
		'date_inscribed'
	)

# admin.site.register(models.HeritageSite)


@admin.register(models.HeritageSiteCategory)
class HeritageSiteCategoryAdmin(admin.ModelAdmin):
	fields = ['category_name']
	list_display = ['category_name']
	ordering = ['category_name']

# admin.site.register(models.HeritageSiteCategory)


@admin.register(models.IntermediateRegion)
class IntermediateRegionAdmin(admin.ModelAdmin):
	fields = ['intermediate_region_name', 'sub_region']
	list_display = ['intermediate_region_name', 'sub_region']
	ordering = ['intermediate_region_name']

# admin.site.register(models.IntermediateRegion)


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
	fields = ['region_name','planet_id']
	list_display = ['region_name','planet_id']
	# ordering = ['region_name']

# admin.site.register(models.Region)


@admin.register(models.SubRegion)
class SubRegionAdmin(admin.ModelAdmin):
	fields = ['sub_region_name', 'region']
	list_display = ['sub_region_name', 'region']
	ordering = ['sub_region_name']

# admin.site.register(models.SubRegion)
