def test_depth_first_mro ( ) : class A ( object , ) : pass class B ( A , ) : pass class C ( A , ) : pass class D ( B , C , ) : pass class E ( D , object , ) : pass class G ( object , ) : pass class H ( G , ) : pass class I ( G , ) : pass class K ( H , I , object , ) : pass class L ( K , E , ) : pass AreEqual ( L . __mro__ , ( L , K , H , I , G , E , D , B , C , A , object ) )