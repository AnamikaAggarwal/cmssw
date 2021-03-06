import FWCore.ParameterSet.Config as cms

#NNPDF30 LO PDF

herwigppPDFSettingsBlock = cms.PSet(

	# PDF for shower
        hwpp_pdf_NNPDF30LO = cms.vstring(
                'create ThePEG::LHAPDF /Herwig/Partons/cmsPDFSet ThePEGLHAPDF.so',			# cmsPDFSet Default name for shower PDF
                'set /Herwig/Partons/cmsPDFSet:PDFName NNPDF30_lo_as_0130.LHgrid',
                'set /Herwig/Partons/cmsPDFSet:RemnantHandler /Herwig/Partons/HadronRemnants',		
                'set /Herwig/Particles/p+:PDF /Herwig/Partons/cmsPDFSet',				# Use PDF in shower
                'set /Herwig/Particles/pbar-:PDF /Herwig/Partons/cmsPDFSet',
        ),

	# PDF for hard subprocess
        hwpp_pdf_NNPDF30LO_Hard = cms.vstring(
                'create ThePEG::LHAPDF /Herwig/Partons/cmsHardPDFSet ThePEGLHAPDF.so',			# cmsHardPDFSet Default name for hard subprocess PDF
                'set /Herwig/Partons/cmsHardPDFSet:PDFName NNPDF30_lo_as_0130.LHgrid',
                'set /Herwig/Partons/cmsHardPDFSet:RemnantHandler /Herwig/Partons/HadronRemnants',		
        ),
)
