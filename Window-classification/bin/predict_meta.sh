predict_meta() {
    oof=$1
    test=$2
    name=$3
    python -u -m src.meta.trainer --inputs-test "${test}" --inputs-oof "${oof}" --output-name ${name} |tee ./meta/${name}.log
}

oof100="[\
    ['./model/model100_total/fold0_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold1_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold2_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold3_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold4_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold5_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold6_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold7_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold8_ep3_valid_tta5.pkl'],\
    ['./model/model100_total/fold9_ep3_valid_tta5.pkl'],\
]"
test100="[\
    ['./model/model100_total/fold0_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold1_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold2_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold3_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold4_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold5_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold6_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold7_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold8_ep3_test_tta5.pkl'],\
    ['./model/model100_total/fold9_ep3_test_tta5.pkl'],\
]"

oof110="[\
    ['./model/model110_total/fold0_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold1_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold2_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold3_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold4_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold5_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold6_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold7_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold8_ep3_valid_tta5.pkl'],\
    ['./model/model110_total/fold9_ep3_valid_tta5.pkl'],\
]"
test110="[\
    ['./model/model110_total/fold0_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold1_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold2_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold3_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold4_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold5_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold6_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold7_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold8_ep3_test_tta5.pkl'],\
    ['./model/model110_total/fold9_ep3_test_tta5.pkl'],\
]"


oof1="[${oof100}, ${oof110}]"
test1="[${test100}, ${test110}]"

predict_meta "${oof1}" "${test1}" meta100

