from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(
    id="grain_elevator",
    prod_cargo_types_with_multipliers=[("GRAI", 1)],
    prob_in_game="3",
    prob_map_gen="15",
    map_colour="50",
    
    # basic grain_elevator doesn't cluster, by design - no industry location checks needed
    prospect_chance="0.75",
    name="string(STR_IND_GRAIN_ELEVATOR)",
    extra_text_fund="string(STR_FUND_ELEVATOR)",
    nearby_station_name="string(STR_STATION_ELEVATOR)",
    fund_cost_multiplier="30",
)

# definitely not in Arctic Basic, grain_elevator has been added and removed more than once from that economy :P

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL"
)

industry.add_tile(
    id="grain_elevator_tile_1",
    location_checks=TileLocationChecks(
        disallow_steep_slopes=True,
        disallow_above_snowline=True,
        disallow_desert=True,
        disallow_coast=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground = industry.add_spriteset(type="empty")
sprite_ground_mud = industry.add_sprite(sprite_number="GROUNDSPRITE_CLEARED")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 52, -31, -21)],
)
spriteset_1_ground = industry.add_spriteset(
    sprites=[(10, 70, 64, 52, -31, -21)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 52, -31, -21)],
)
spriteset_2_ground = industry.add_spriteset(
    sprites=[(80, 70, 64, 52, -31, -21)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 52, -31, -21)],
)
spriteset_3_ground = industry.add_spriteset(
    sprites=[(150, 70, 64, 52, -31, -21)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 52, -31, -21)],
)
spriteset_4_ground = industry.add_spriteset(
    sprites=[(220, 70, 64, 52, -31, -21)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 52, -31, -21)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 52, -31, -21)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 52, -31, -21)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 52, -31, -21)],
)

industry.add_spritelayout(
    id="grain_elevator_spritelayout_1",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_1_ground,
    building_sprites=[spriteset_1],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="grain_elevator_spritelayout_2",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_2_ground,
    building_sprites=[spriteset_2],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="grain_elevator_spritelayout_3",
    tile="grain_elevator_tile_1",
    ground_sprite=sprite_ground_mud,
    ground_overlay=spriteset_3_ground,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="grain_elevator_spritelayout_4",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_4_ground,
    building_sprites=[spriteset_4],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="grain_elevator_spritelayout_5",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="grain_elevator_spritelayout_6",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="grain_elevator_spritelayout_7",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    terrain_aware_ground=True,
)
industry.add_spritelayout(
    id="grain_elevator_spritelayout_8",
    tile="grain_elevator_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    terrain_aware_ground=True,
)

industry.add_industry_layout(
    id="grain_elevator_industry_layout_1",
    layout=[
        (0, 2, "grain_elevator_spritelayout_8"),
        (0, 3, "grain_elevator_spritelayout_3"),
        (1, 0, "grain_elevator_spritelayout_2"),
        (2, 0, "grain_elevator_spritelayout_1"),
        (2, 2, "grain_elevator_spritelayout_5"),
        (2, 3, "grain_elevator_spritelayout_7"),
        (3, 2, "grain_elevator_spritelayout_6"),
        (3, 3, "grain_elevator_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="grain_elevator_industry_layout_2",
    layout=[
        (0, 0, "grain_elevator_spritelayout_4"),
        (0, 2, "grain_elevator_spritelayout_7"),
        (0, 3, "grain_elevator_spritelayout_6"),
        (1, 0, "grain_elevator_spritelayout_5"),
        (1, 3, "grain_elevator_spritelayout_1"),
        (2, 0, "grain_elevator_spritelayout_8"),
        (2, 1, "grain_elevator_spritelayout_3"),
        (2, 2, "grain_elevator_spritelayout_2"),
    ],
)
industry.add_industry_layout(
    id="grain_elevator_industry_layout_3",
    layout=[
        (0, 0, "grain_elevator_spritelayout_8"),
        (0, 1, "grain_elevator_spritelayout_1"),
        (0, 2, "grain_elevator_spritelayout_5"),
        (1, 0, "grain_elevator_spritelayout_2"),
        (1, 2, "grain_elevator_spritelayout_3"),
        (2, 0, "grain_elevator_spritelayout_7"),
        (3, 0, "grain_elevator_spritelayout_4"),
        (3, 2, "grain_elevator_spritelayout_6"),
    ],
)
