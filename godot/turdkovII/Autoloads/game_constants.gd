extends Node

enum ItemSpawnMethod {
	MAP,
	TRADER,
	AI,
	QUEST,
	CRAFT,
	PLAYER,   # Items that spawn on a player (e.g. player scav)
	SPECIAL,  # Starter items, items from promo keys, etc.
	MANUAL,   # Admin/debug spawn menu
}

enum Maps {
	SHORELINE,
	INTERCHANGE,
	CUSTOMS,
	FACTORY,
	LABS,
	WOODS,
	RESORT,
	LIGHTHOUSE,
	STREETS,
	GROUNDZERO
}

enum MapSpawnType {
	CONTAINER,
	LOOSE,
	SAFE,
	AIRDROP,
	KEYROOM_CONTAINER,
	KEYROOM_LOOSE,
}

enum Traders {
	PRAPOR,
	THERAPIST,
	FENCE,
	SKIER,
	PEACEKEEPER,
	MECHANIC,
	RAGMAN,
	JAEGER,
	LIGHTKEEPER,
}

enum TraderSpawnType {
	PURCHASE,
	BARTER,
	QUEST,
}

enum QuestItemType {
	EQUIPMENT_GIVEN,
	EQUIPMENT_LOOTED,
	REWARD,
}

enum AIType {
	REGULAR,
	SNIPER,
	GUARD,
	RAIDER,
	KILLA,
	TAGILLA,
}

enum SpecialSpawnType {
	STARTER,
	SCAV_JUNKBOX,
	PROMO_KEY,
}

