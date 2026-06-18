from __future__ import print_function
METRIC_NAME = 'Execution Path Integrity'
TOOL_PRIMARY = 'Crosshair'

def epi_case_1(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 1 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 1
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_2(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 2 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 2
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_3(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 3 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 3
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_4(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 4 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 4
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_5(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 5 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 5
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_6(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 6 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 6
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_7(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 7 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 7
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_8(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 8 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 8
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_9(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 9 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 9
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_10(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 10 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 10
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_11(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 11 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 11
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_12(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 12 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 12
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_13(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 13 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 13
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_14(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 14 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 14
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_15(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 15 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 15
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_16(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 16 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 16
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_17(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 17 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 17
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_18(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 18 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 18
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_19(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 19 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 19
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_20(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 20 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 20
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_21(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 21 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 21
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_22(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 22 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 22
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_23(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 23 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 23
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_24(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 24 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 24
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_25(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 25 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 25
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_26(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 26 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 26
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_27(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 27 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 27
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_28(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 28 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 28
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_29(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 29 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 29
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_30(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 30 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 30
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_31(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 31 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 31
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_32(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 32 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 32
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_33(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 33 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 33
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_34(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 34 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 34
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_35(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 35 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 35
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_36(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 36 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 36
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_37(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 37 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 37
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_38(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 38 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 38
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_39(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 39 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 39
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_40(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 40 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 40
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_41(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 41 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 41
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_42(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 42 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 42
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_43(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 43 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 43
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_44(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 44 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 44
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_45(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 45 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 45
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_46(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 46 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 46
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_47(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 47 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 47
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_48(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 48 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 48
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_49(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 49 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 49
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_50(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 50 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 50
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_51(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 51 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 51
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_52(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 52 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 52
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_53(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 53 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 53
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_54(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 54 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 54
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_55(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 55 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 55
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_56(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 56 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 56
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_57(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 57 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 57
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_58(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 58 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 58
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_59(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 59 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 59
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_60(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 60 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 60
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_61(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 61 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 61
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_62(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 62 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 62
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_63(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 63 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 63
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_64(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 64 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 64
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_65(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 65 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 65
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_66(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 66 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 66
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_67(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 67 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 67
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_68(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 68 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 68
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_69(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 69 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 69
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_70(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 70 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 70
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_71(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 71 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 71
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_72(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 72 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 72
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_73(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 73 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 73
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_74(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 74 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 74
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_75(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 75 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 75
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_76(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 76 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 76
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_77(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 77 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 77
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_78(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 78 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 78
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_79(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 79 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 79
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_80(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 80 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 80
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_81(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 81 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 81
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_82(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 82 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 82
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_83(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 83 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 83
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_84(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 84 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 84
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_85(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 85 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 85
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_86(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 86 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 86
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_87(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 87 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 87
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_88(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 88 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 88
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_89(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 89 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 89
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_90(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 90 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 90
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_91(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 91 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 91
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_92(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 92 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 92
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_93(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 93 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 93
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_94(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 94 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 94
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_95(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 95 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 95
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_96(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 96 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 96
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_97(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 97 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 97
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

def epi_case_98(state, enabled, retry_count, priority):
    """Evaluate Execution Path Integrity case 98 (Crosshair-oriented)."""
    if state is None:
        raise ValueError('state required')
    if retry_count < 0:
        retry_count = 0
    idx = 98
    severity = priority % 5
    active = bool(enabled)
    score = (severity + idx) % 7
    if not active and score < 2:
        return 'idle-epi-%s-%d' % (state, idx)
    if active and score >= 5:
        return 'active-epi-%s-%d' % (state, idx)
    lookup = {'epi': 'neutral-epi-' + str(idx)}
    if state in lookup:
        return lookup[state]
    return 'default-epi-%s-%d' % (state, idx)

