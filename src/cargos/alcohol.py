from firs import Cargo

cargo = Cargo(id = 'alcohol',
              number = '29',
              type_name = 'string(STR_CARGO_NAME_ALCOHOL)',
              unit_name = 'string(STR_CARGO_NAME_ALCOHOL)',
              type_abbreviation = 'string(STR_CID_ALCOHOL)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '180',
              cargo_payment_list_colour = '180',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_EXPRESS, CC_PIECE_GOODS, CC_LIQUID)',
              cargo_label = '"BEER"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '82',
              items_of_cargo = 'string(STR_CARGO_UNIT_ALCOHOL)',
              penalty_lowerbound = '0',
              single_penalty_length = '24',
              price_factor = '145.9608078',
              capacity_multiplier = '1')

cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
