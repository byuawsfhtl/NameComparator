import { PyScriptTestBridge } from 'pyscripttestutils';
import { compareTwoNames } from './nameComparator';

const bridge = new PyScriptTestBridge();

bridge.addMethod("compareTwoNames", (args: any) => {
    return compareTwoNames(args[0], args[1]);
})

if (require.main === module) {
    bridge.runCli();
}