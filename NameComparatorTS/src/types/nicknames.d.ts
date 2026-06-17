// Type definitions for nickname data

// Structure for nicknameToId.json
declare module "../../data/nicknames/nicknameToId.json" {
    const data: { [nickname: string]: number[] };
    export default data;
}

// Structure for name_variants.json
declare module "../../data/nicknames/nameVariants.json" {
    const data: { [id: number]: string[] };
    export default data;
} 