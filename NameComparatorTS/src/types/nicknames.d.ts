// Type definitions for nickname data

// Structure for nicknameToId.json
declare module "../../data/nicknames/nicknameTold.json" {
    const data: { [nickname: string]: number[] };
    export default data;
}

// Structure for name_variants.json
declare module "../../data/nicknames/name_variants.json" {
    const data: { [id: number]: string[] };
    export default data;
} 