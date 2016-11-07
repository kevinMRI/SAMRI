import preprocessing, glm

def composite_workflow():
	glm.l1("~/NIdata/ofM.dr/preprocessing/composite", workflow_name="composite", include={"subjects":[i for i in range(4001,4010)]+[4011,4012]}, habituation="confound",mask="/home/chymera/NIdata/templates/ds_QBI_chr_bin.nii.gz",keep_work=True)
	glm.l1("~/NIdata/ofM.dr/preprocessing/composite", workflow_name="composite_dr", include={"subjects":[i for i in range(4001,4010)]+[4011,4012]}, habituation="confound",mask="/home/chymera/NIdata/templates/roi/f_dr_chr_bin.nii.gz",)
	glm.l2_common_effect("~/NIdata/ofM.dr/l1/composite", workflow_name="subjectwise_composite", groupby="subject")
	glm.l2_common_effect("~/NIdata/ofM.dr/l1/composite", workflow_name="sessionwise_composite", groupby="session", exclude={"subjects":["4001","4002","4003","4004","4005","4006","4009","4011","4013"]})
	glm.l2_common_effect("~/NIdata/ofM.dr/l1/composite", workflow_name="sessionwise_composite_w4011", groupby="session", exclude={"subjects":["4001","4002","4003","4004","4005","4006","4009","4013"]})


if __name__ == '__main__':
	composite_workflow()
