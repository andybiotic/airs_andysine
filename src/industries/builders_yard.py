from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="builders_yard",
    accept_cargo_types=[
        "BDMT",
    ],
    prod_cargo_types=[],
    prob_in_game="0",  # do not build during gameplay
    prob_map_gen="8",
    prod_multiplier="[0, 0]",
    map_colour="121",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    prospect_chance="0.75",  # yeah delete this, it's not required for tertiary
    name="string(STR_IND_BUILDERS_YARD)",
    nearby_station_name="string(STR_STATION_MERCHANTS_LANE)",
    fund_cost_multiplier="16",
    provides_snow=True,
)

industry.enable_in_economy(
    "PLAINS_TRAINS_AND_STEEL",
    accept_cargo_types=[
        "CMNT",
        "BDMT",
    ],
    fund_cost_multiplier="4",
)

industry.enable_in_economy(
    "BLACK_GOLD_AND_FIRE",
    accept_cargo_types=[
        "BDMT",
    ],
    fund_cost_multiplier="4",
)

industry.enable_in_economy(
    "TRADE_AND_WAVES",
    accept_cargo_types=[
        "CMNT",
        "BDMT",
    ],
    fund_cost_multiplier="4",
)

industry.add_tile(
    id="builders_yard_tile_1",
    location_checks=TileLocationChecks(
        require_houses_nearby=True,
        require_effectively_flat=True,
        disallow_industry_adjacent=True,
    ),
)

spriteset_ground = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
stacks_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 56, -31, -26)],
)
shed = industry.add_spriteset(
    sprites=[(80, 10, 64, 56, -31, -26)],
)
silo = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -34)],
)
stacks_2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 56, -31, -26)],
)
industry.add_spritelayout(
    id="builders_yard_spritelayout_1",
    tile="builders_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[stacks_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="builders_yard_spritelayout_2",
    tile="builders_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[shed],
)
industry.add_spritelayout(
    id="builders_yard_spritelayout_3",
    tile="builders_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[silo],
)
industry.add_spritelayout(
    id="builders_yard_spritelayout_4",
    tile="builders_yard_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[stacks_2],
)

industry.add_industry_layout(
    id="builders_yard_industry_layout_1",
    layout=[
        (0, 0, "builders_yard_spritelayout_3"),
        (0, 1, "builders_yard_spritelayout_4"),
        (1, 0, "builders_yard_spritelayout_2"),
        (1, 1, "builders_yard_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="builders_yard_industry_layout_2",
    layout=[
        (0, 0, "builders_yard_spritelayout_2"),
        (0, 1, "builders_yard_spritelayout_3"),
        (1, 0, "builders_yard_spritelayout_4"),
        (1, 1, "builders_yard_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="builders_yard_industry_layout_3",
    layout=[
        (0, 0, "builders_yard_spritelayout_3"),
        (0, 1, "builders_yard_spritelayout_2"),
        (1, 0, "builders_yard_spritelayout_1"),
        (1, 1, "builders_yard_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="builders_yard_industry_layout_4",
    layout=[
        (0, 0, "builders_yard_spritelayout_2"),
        (0, 1, "builders_yard_spritelayout_1"),
        (1, 0, "builders_yard_spritelayout_3"),
        (1, 1, "builders_yard_spritelayout_4"),
    ],
)
