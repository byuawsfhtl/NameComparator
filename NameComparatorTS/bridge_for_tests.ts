import { PyScriptTestBridge } from 'pyscripttestutils';
import { compareTwoNames } from './nameComparator.js';
import { extrapolateBestFullName } from './src/nameExtrapolation.js';
import { fileURLToPath } from 'url';

const bridge = new PyScriptTestBridge();

bridge.addMethod("compareTwoNames", (args: any) => {
    return compareTwoNames(args[0], args[1]);
})

bridge.addMethod("extrapolateBestFullName", (args: any) => {
    return extrapolateBestFullName(args[0]);
})

if (fileURLToPath(import.meta.url) === process.argv[1]) {
    bridge.runCli();
}