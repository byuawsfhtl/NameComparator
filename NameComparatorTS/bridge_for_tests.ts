import { PyScriptTestBridge } from 'pyscripttestutils';
import { compareTwoNames } from './nameComparator.js';
import { fileURLToPath } from 'url';

const bridge = new PyScriptTestBridge();

bridge.addMethod("compareTwoNames", (args: any) => {
    return compareTwoNames(args[0], args[1]);
})

if (fileURLToPath(import.meta.url) === process.argv[1]) {
    bridge.runCli();
}