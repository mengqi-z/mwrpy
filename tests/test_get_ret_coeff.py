import numpy as np
from numpy.testing import assert_array_almost_equal

from mwrpy.level2.get_ret_coeff import get_mvr_coeff

FREQ = np.array(
    [
        22.24,
        23.04,
        23.84,
        25.44,
        26.24,
        27.84,
        31.4,
        51.26,
        52.28,
        53.86,
        54.94,
        56.66,
        57.3,
        58.0,
    ]
)
SITE = "hyytiala"


def test_coefficients():
    test_data = {
        "lwp": {
            "DY": ((1, 1, 1), (1,)),
            "PS": ((1, 1, 1), (1,)),
            "DB": ((1, 1, 1), (1,)),
            "RT": ((2, 2, 2), (1,)),
            "VN": ((110, 110, 110), (1,)),
            "ND": ((9, 4, 6.5), (2,)),
            "FR": ((23.04, 58, 41.699997), (13,)),
            "AG": ((90, 4.2, 27.473684), (19,)),
            "NP": ((0.025999999, 0.025999999, 0.025999999), (19, 1)),
            "input_offset": ((61.404, -5.174205e-05, 6337.0576), (19, 16)),
            "input_scale": ((0.01880088, 1.0000551, 0.14415415), (19, 16)),
            "output_offset": ((1.25075, 17.077847, 5.906157), (19, 1)),
            "output_scale": ((1.6676667, 22.770462, 7.8748765), (19, 1)),
            "W1": ((-107.37779, -2.3326364, -0.7625811), (17, 9, 19)),
            "W2": ((-10.072118, -9.450926, -2.7468667), (19, 10)),
            "RM": ((0.00434408, 0.19351903, 0.041093733), (19, 1)),
            "FR_BL": ((23.04, 58.0, 41.699997), (13,)),
            "retrieval_elevation_angles": ((90.0, 4.199999, 27.473684), (19,)),
            "retrieval_frequencies": ((23.04, 58.0, 41.69999), (13,)),
        },
        "iwv": {
            "DY": ((1, 1, 1), (1,)),
            "PS": ((1, 1, 1), (1,)),
            "DB": ((1, 1, 1), (1,)),
            "RP": ((1, 1, 1), (1,)),
            "RT": ((2, 2, 2), (1,)),
            "VN": ((110, 110, 110), (1,)),
            "ND": ((9, 4, 6.5), (2,)),
            "FR": ((23.04, 58, 41.699997), (13,)),
            "AG": ((90, 4.2, 27.473684), (19,)),
            "NP": ((0.025999999, 0.025999999, 0.025999999), (19, 1)),
            "input_offset": ((61.404, -5.174205e-05, 6337.0576), (19, 16)),
            "input_scale": ((0.01880088, 1.0000551, 0.14415415), (19, 16)),
            "output_offset": ((24.4429, 333.74542, 115.42163), (19, 1)),
            "output_scale": ((31.616266, 431.6912, 149.29494), (19, 1)),
            "W1": ((-4.5245423, -0.9779363, -0.6337075), (17, 9, 19)),
            "W2": ((-8.668256, 10.204778, -3.7813265), (19, 10)),
            "RM": ((0.088511630, 3.4751670360, 0.7352865), (19, 1)),
            "FR_BL": ((23.04, 58.0, 41.699997), (13,)),
            "retrieval_elevation_angles": ((90.0, 4.199999, 27.473684), (19,)),
            "retrieval_frequencies": ((23.04, 58.0, 41.69999), (13,)),
        },
        "tpt": {
            "DY": ((1, 1, 1), (1,)),
            "PS": ((1, 1, 1), (1,)),
            "DB": ((1, 1, 1), (1,)),
            "RP": ((4, 4, 4), (1,)),
            "RT": ((2, 2, 2), (1,)),
            "VN": ((110, 110, 110), (1,)),
            "ND": ((12, 4, 8), (2,)),
            "FR": ((23.04, 58, 41.699997), (13,)),
            "AG": ((90, 90, 90), (1,)),
            "AL": ((0.0, 10000.0, 2875.806396484375), (93,)),
            "NP": ((0.025999999, 0.025999999, 0.025999999), (1,)),
            "input_offset": ((61.4039993286, -5.1742048e-05, 6304.670410), (1, 16)),
            "input_scale": ((0.01880088, 1.00005507, 0.146652624), (1, 16)),
            "output_offset": ((271.200012, 219.82550, 259.26358), (1, 93)),
            "output_scale": ((44.4666671, 24.967332, 32.562801), (1, 93)),
            "W1": ((-60.5274200, 6.1980004, -2.25016403), (17, 12, 1)),
            "W2": ((6.22275257, 1.43107211, -1.814291954), (93, 13, 1)),
            "RM": ((2.035391330, 3.3711481, 1.282065437), (93, 1)),
            "FR_BL": ((23.04, 58.0, 41.699997), (13,)),
            "retrieval_elevation_angles": ((90.0, 90, 90), (1,)),
            "retrieval_frequencies": ((23.04, 58.0, 41.69999), (13,)),
        },
        "tpb": {
            "DY": ((1, 1, 1), (1,)),
            "PS": ((1, 1, 1), (1,)),
            "DB": ((1, 1, 1), (1,)),
            "RP": ((5, 5, 5), (1,)),
            "RT": ((2, 2, 2), (1,)),
            "VN": ((110, 110, 110), (1,)),
            "ND": ((15, 4, 9.5), (2,)),
            "FR": ((23.04, 58, 41.699997), (13,)),
            "AG": ((90.0, 4.199999809265137, 19.440000534057617), (10,)),
            "AL": ((0.0, 10000.0, 2875.806396484375), (93,)),
            "NP": ((0.025999999, 0.025999999, 0.025999999), (1,)),
            "input_offset": ((61.40399932, -5.1742048e-05, 945.881530), (133,)),
            "input_scale": ((0.01880088, 1.00005507, 0.0258186), (133,)),
            "output_offset": ((271.200012, 219.8255, 259.26358), (93,)),
            "output_scale": ((44.4666671, 24.96733, 32.56280), (93,)),
            "W1": ((-149.7417449, 0.19153261, -0.0740887), (134, 15)),
            "W2": ((4.33258, -0.72129, -1.55458), (93, 16)),
            "RM": ((0.8922356963, 3.0863358, 1.051631445), (93, 1)),
            "FR_BL": ((23.04, 58.0, 41.699997), (13,)),
            "retrieval_elevation_angles": ((90.0, 4.199999, 19.44), (10,)),
            "retrieval_frequencies": ((23.04, 58.0, 41.699997), (13,)),
        },
        "hpt": {
            "DY": ((1, 1, 1), (1,)),
            "PS": ((1, 1, 1), (1,)),
            "DB": ((1, 1, 1), (1,)),
            "RP": ((3, 3, 3), (1,)),
            "RT": ((2, 2, 2), (1,)),
            "VN": ((110, 110, 110), (1,)),
            "ND": ((9, 4, 6.5), (2,)),
            "FR": ((23.04, 58, 41.699997), (13,)),
            "AG": ((90.0, 90, 90), (1,)),
            "AL": ((0.0, 10000.0, 2875.806396484375), (93,)),
            "NP": ((0.025999999, 0.025999999, 0.025999999), (1,)),
            "input_offset": ((61.403999328, -5.17420485e-05, 6304.67041), (1, 16)),
            "input_scale": ((0.018800880, 1.00005507, 0.14665262), (1, 16)),
            "output_offset": ((9.317116737, 0.0755304, 4.9657354), (1, 93)),
            "output_scale": ((12.17451095, 0.1005687192082, 6.555077552), (1, 93)),
            "W1": ((-22.01639366149, -2.077390670776, -4.22366380691), (17, 9, 1)),
            "W2": ((-6.617764472961, -5.96833944320, -4.42309951782), (93, 10, 1)),
            "RM": ((0.783515751, 0.00679313, 0.440780830021), (93, 1)),
            "FR_BL": ((23.04, 58.0, 41.699997), (13,)),
            "retrieval_elevation_angles": ((90.0, 90, 90), (1,)),
            "retrieval_frequencies": ((23.04, 58.0, 41.69999), (13,)),
        },
    }

    for key, item in test_data.items():
        data = get_mvr_coeff(SITE, key, FREQ, None)
        data = get_mvr_coeff(SITE, key, FREQ, None)
        if key == "lwp":
            expected = np.array(
                [-107.37779, -30.645275, -76.23844, 0.9421638, -27.80052],
                dtype=np.float32,
            )
            assert_array_almost_equal(data[0]["W1"].flatten()[:5], expected)
        for name, value in data[0].items():
            shape: tuple
            if isinstance(value, str):
                continue
            if name not in item:
                first, last, mean = 0.0, 0.0, 0.0
                shape = (1,)
            else:
                first, last, mean = item[name][0]
                shape = item[name][1]
            # print(key, name, first, last, mean, shape)
            _check(name, value, float(first), float(last), float(mean), shape=shape)


def _check(
    key: str,
    data: np.ndarray,
    first: float,
    last: float,
    mean_value: float,
    shape: tuple,
):
    assert data.ndim in (1, 2, 3)
    if data.ndim == 1:
        first_value = data[0]
        last_value = data[-1]
    elif data.ndim == 2:
        first_value = data[0, 0]
        last_value = data[-1, -1]
    else:
        first_value = data[0, 0, 0]
        last_value = data[-1, -1, -1]

    if isinstance(first_value, str):
        return

    # print(key, f"{first_value}, {last_value}, {np.mean(data)}, {first}, {last}, {mean_value}, {shape}, {data.shape}")

    assert_array_almost_equal(first_value, first, decimal=4)
    assert_array_almost_equal(last_value, last, decimal=4)
    assert_array_almost_equal(np.mean(data), mean_value, decimal=4)
    assert data.shape == shape
